# Homeassistant MQTT for python with discovery

This project is a fork from https://gitlab.com/anphi/homeassistant-mqtt-binding with some changes in the logic.
Changes are described below.

This package enables you to implement arbitrary devices in python supported in homeassistant. The communication with
homeassistant is handled by MQTT. For example you could write an simple program running on a raspberry pi controlling an
LED. By exposing this configuration to homeassistant you can easily control the LED via HA.

The base class handles the following things:

* registering devices in homeassistant through the mqtt discovery protocol by using the <config> topic
* setting the device as available once fully setup
* setting the device unavailable when quitting the application

### Installation

`python3 -m pip install homeassistant-mqtt-devices`
the dependencies should be installed automatically

## Usage

1. create an paho mqtt Client instance connected to your mqtt server, possibly within a try / restart loop to handle disconnections.
2. instantiate your desired device and pass the Client instance to the constructor
3. when your program closes make sure to call the `close()` function of each device for cleanup

## Examples

The following examples require an already running stack of homeassistant and an MQTT server.  
See the [examples](https://gitlab.com/anphi/homeassistant-mqtt-binding/HaMqtt/examples) folder for all demo scripts.

* switch.py:
  simple switch device that can be toggled by homeassistant
* temperature.py:
  simple sensor device that pushed info to homeassistant

## Expanding the application

Since I don't use all devices I haven't implemented them yet. You can easily implement any missing device:

1. create an empty class subclassing any of the devices (normally you would subclass `MQTTDevice` or `MQTTSensor`).
2. implement the `initialize()` function. It gets called in the parent constructor right before it sends out the
   discovery payload to the broker. Use `add_config_option()` to add your own settings to the configuration dictionary.
3. Implement any callbacks that might be necessary for all devices that can receive data. (commands for switches for
   example).
4. If your device needs more topics than state, configuration and set, feel free to implement them

## Changes from the original library from anphi

### Notes

* Code compatibility is preserved as much as possible , opening the way to a re-merge later
* This repo has been made as a way to experiment on my own issues. It has no mean to replace the original one.

### Modifications

1. Devices Classes are given as str and not as classes, since in HomeAssistant there are added classes all the time. Default is "None".
2. Dé-correlate the creation of the class and the sending of the "config" topic , to allow the user code to add or modify the conf_dict before sending it to MQTT.
   Thus a "send_discovery()" shall be used before pushing data. However to keep compatibility, this method is call before the first call to "publish_state()" if it has not be done before.
3. The send_discovery() is re-sent a periodic intervals (default is 30mn) - this is usefull when the MQTT server or HA become unreachable for a while.
4. Default value for send_initial parameter is False : Sending a "0" value for some meters do impact statistical calculations

  ... more to come 
