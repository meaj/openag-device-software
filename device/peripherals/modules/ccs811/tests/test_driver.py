# Import standard python libraries
import sys, os

# Get current working directory
cwd = os.getcwd()
print("Running test from: {}".format(cwd))

# Set correct import path
if cwd.endswith("sht25"):
    print("Running test locally")
    os.chdir("../../../../")
elif cwd.endswith("openag-device-software"):
    print("Running test globally")
else:
    print("Running test from invalid location")
    sys.exit(0)

# Import manager
from device.peripherals.modules.sht25.driver import SHT25Driver


def test_init():
    driver = SHT25Driver(name="Test", bus=2, address=0x77, simulate=True)


def test_read_temperature():
    driver = SHT25Driver("Test", 2, 0x77, simulate=True)
    temperature, error = driver.read_temperature()
    assert error.exists() == False
    assert temperature == -47.0


def test_read_humidity():
    driver = SHT25Driver("Test", 2, 0x77, simulate=True)
    humidity, error = driver.read_humidity()
    assert error.exists() == False
    assert humidity == -6.0


def test_read_user_register():
    driver = SHT25Driver("Test", 2, 0x77, simulate=True)
    user_register, error = driver.read_user_register()
    assert error.exists() == False
    assert user_register.end_of_battery == False
    assert user_register.heater_enabled == False
    assert user_register.reload_disabled == False


def test_reset():
    driver = SHT25Driver("Test", 2, 0x77, simulate=True)
    error = driver.reset()
    assert error.exists() == False