# This is a sample Python script.

# Press Shift + F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sensors
import time

CPU_CHIP = 'k10temp-pci-00c3'

sensors.init()


def poll_sensors(iterations):
    try:
        for i in range(iterations):
            print(f'Read number {i + 1}')
            chips = sensors.iter_detected_chips()
            for chip in chips:
                chip_name = str(chip)
                if chip_name == CPU_CHIP:
                    print(f'Chip name: {chip_name}')
                    for feature in chip:
                        if 'T' in feature.label:
                            print(feature.label, feature.get_value())
                    time.sleep(1.5)
    finally:
        sensors.cleanup()


if __name__ == '__main__':
    poll_sensors(15)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
