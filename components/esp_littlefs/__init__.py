"""ESPHome external component wrapper for joltwallet/esp_littlefs."""
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import component
from esphome.const import CONF_ID
from esphome.cpp_types import ESPIDFComponent

DEPENDENCIES = ["esp32"]
CODEOWNERS = ["@yourusername"]
AUTO_LOAD = ["littlefs"]

littlefs_ns = cg.esphome_ns.namespace("littlefs")
LittleFSComponent = ESPIDFComponent(littlefs_ns, "littlefs_component")

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(LittleFSComponent),
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

