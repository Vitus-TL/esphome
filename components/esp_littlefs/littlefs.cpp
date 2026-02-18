#include "littlefs.h"
#include "esphome/log.h"
#include "esp_littlefs.h"

namespace esphome {
namespace littlefs {

static const char *const TAG = "littlefs";

void LittleFSComponent::setup() {
  ESP_LOGCONFIG(TAG, "Setting up LittleFS...");
  
  esp_vfs_littlefs_conf_t conf = {
      .base_path = "/littlefs",
      .partition_label = "littlefs",
      .format_if_mount_failed = true,
  };
  
  esp_err_t ret = esp_vfs_littlefs_register(&conf);
  if (ret != ESP_OK) {
    ESP_LOGE(TAG, "Mount failed: %s", esp_err_to_name(ret));
  } else {
    ESP_LOGI(TAG, "LittleFS mounted at /littlefs");
  }
}

}  // namespace littlefs
}  // namespace esphome

