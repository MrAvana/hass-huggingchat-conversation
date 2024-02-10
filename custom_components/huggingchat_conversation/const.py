"""Constants for the HuggingChat Conversation integration."""

DOMAIN = "huggingchat_conversation"
CONF_EMAIL = "email"
DEFAULT_EMAIL = "YOUR_EMAIL"
CONF_PASSWORD = "password"
DEFAULT_PASSWORD = "YOUR_PASSWORD"
CONF_CHAT_MODEL = "chat_model"
DEFAULT_CHAT_MODEL = 0
CONF_PROMPT = "prompt"
DEFAULT_PROMPT = """This smart home is controlled by Home Assistant.

An overview of the areas and the devices in this smart home:
{%- for area in areas() %}
  {%- set area_info = namespace(printed=false) %}
  {%- if not area_info.printed %}

{{ area_name(area) }}:
        {%- set area_info.printed = true %}
  {%- endif %}
  {%- if area_devices(area) %}
- Devices:
    {%- for device in area_devices(area) -%}
      {%- if not device_attr(device, "disabled_by") and not device_attr(device, "entry_type") and device_attr(device, "name") %}
  - {{ device_attr(device, "name") }}{% if device_attr(device, "model") and (device_attr(device, "model") | string) not in (device_attr(device, "name") | string) %} ({{ device_attr(device, "model") }}){% endif %}
      {%- endif %}
    {%- endfor %}
  {%- else %}
No devices in this area
  {%- endif %}

  {%- if area_entities(area) %}

- Entities
    {%- for entity in area_entities(area) | reject('is_hidden_entity') -%}
      {%- if not entity.is_hidden_entity %}
  - {{ state_attr(entity, 'friendly_name') }} ({{ entity }}){%- if states(entity) != "unknown" %}: {{ states(entity) }}{% endif %}
      {%- endif %}
    {%- endfor %}
  {%- else %}

No entities in this area
  {%- endif %}
{%- endfor %}

Answer the user's questions about the world truthfully.

If the user wants to control a device, reject the request and suggest using the Home Assistant app.
"""
