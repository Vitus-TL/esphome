"""ESPHome external component wrapper for joltwallet/esp_littlefs."""
import os
import shutil
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID
from esphome.core import CORE

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

    # Copy esp_littlefs.h into src/ so it's findable via -Isrc
    component_dir = os.path.dirname(os.path.abspath(__file__))
    src_header = os.path.join(component_dir, "include", "esp_littlefs.h")
    dest_header = CORE.relative_src_path("esp_littlefs.h")
    shutil.copy2(src_header, dest_header)

    cg.add_define("USE_ESP_LITTLEFS")
