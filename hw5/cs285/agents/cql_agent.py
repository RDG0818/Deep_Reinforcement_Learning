from typing import Sequence, Callable, Tuple, Optional

import torch
from torch import nn

import numpy as np

import cs285.infrastructure.pytorch_util as ptu
from cs285.agents.dqn_agent import DQNAgent


class CQLAgent(DQNAgent):
    def __init__(
        self,
        observation_shape: Sequence[int],
        num_actions: int,
        cql_alpha: float,
        cql_temperature: float = 1.0,
        **kwargs,
    ):
        super().__init__(
            observation_shape=observation_shape, num_actions=num_actions, **kwargs
        )
        self.cql_alpha = cql_alpha
        self.cql_temperature = cql_temperature

    def compute_critic_loss(
        self,
        obs: torch.Tensor,
        action: torch.Tensor,
        reward: torch.Tensor,
        next_obs: torch.Tensor,
        done: bool,
    ) -> Tuple[torch.Tensor, dict, dict]:
        loss, metrics, variables = super().compute_critic_loss(
            obs,
            action,
            reward,
            next_obs,
            done,
        )

        qa_values = variables["qa_values"]  # Q-values for the actual actions taken
        q_values = variables["q_values"]  # Q-values for all actions

        # Ensure q_values is 2D
        if q_values.dim() == 1:
            q_values = q_values.unsqueeze(0)  # Add batch dimension if missing
        
        # Compute logsumexp over all actions
        logsumexp_q_values = torch.logsumexp(q_values / self.cql_temperature, dim=1)

        # Compute CQL regularization
        cql_reg = (logsumexp_q_values - qa_values.squeeze()).mean()

        # TODO(student): modify the loss to implement CQL
        # Hint: `variables` includes qa_values and q_values from your CQL implementation
        loss = loss + self.cql_alpha * cql_reg

        # Add CQL regularization to metrics for logging
        metrics['cql_reg'] = cql_reg.item()

        return loss, metrics, variables
