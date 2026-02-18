#pragma once
#include "esphome/core/component.h"
#include "esp_littlefs.h"  // Your existing header

namespace esphome {
namespace littlefs {

class LittleFSComponent : public Component {
 public:
  void setup() override;
};

}  // namespace littlefs
}  // namespace esphome

