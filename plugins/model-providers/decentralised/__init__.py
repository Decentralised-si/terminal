"""Decentralised.si provider profile: the network's OpenAI-compatible API (DSI Axon).

One ``ds_`` key reaches every model the network routes to: open models on community
GPU nodes, hosted open models, and commercial models through the account's own vendor
keys. ``auto`` lets the blind router pick per conversation.
"""

from providers import register_provider
from providers.base import ProviderProfile

decentralised = ProviderProfile(
    name="decentralised",
    aliases=("dsi", "decentralised-si", "decentralized", "decentralise"),
    display_name="Decentralised.si",
    description="Decentralised.si network — one key, every model, routed for you",
    signup_url="https://decentralised.si/app#/console/keys",
    env_vars=("DSI_API_KEY", "DSI_BASE_URL"),
    base_url="https://api.decentralised.si/openai/v1",
    auth_type="api_key",
    # Tell the router this is an agent session; it keeps a conversation on one provider.
    default_headers={"x-decentralise-client": "dsi-agent-terminal"},
    # Default: a long-context open model with reliable tool calling (GLM 5.3 Flash on Workers AI).
    # "auto" lets the router choose; agent-grade hosted models need naming explicitly today.
    fallback_models=("@cf/zai-org/glm-5.3-flash", "@cf/deepseek-ai/deepseek-v4-flash-0731", "@cf/moonshotai/kimi-k2.7-code", "auto"),
    default_aux_model="@cf/zai-org/glm-5.3-flash",
)

register_provider(decentralised)
