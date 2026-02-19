"""ESPHome external component wrapper for joltwallet/esp_littlefs."""
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import esp32
from esphome.const import CONF_ID
import os

DEPENDENCIES = ["esp32"]
CODEOWNERS = ["@VitusTL"]

AUTO_LOAD = []

littlefs_ns = cg.esphome_ns.namespace("littlefs")
LittleFSComponent = littlefs_ns.class_("LittleFSComponent", cg.Component)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(LittleFSComponent),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    # Expose the include directory so user code can #include "esp_littlefs.h"
    component_dir = os.path.dirname(os.path.abspath(__file__))
    include_dir = os.path.join(component_dir, "include")
    cg.add_build_flag(f"-I{include_dir}")

    cg.add_define("USE_ESP_LITTLEFS")
