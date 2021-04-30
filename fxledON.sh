#!/bin/bash
curl -X POST -H "Content-type: application/json" -d '{"type":"wavelength(Reactive)","config":{"config":{"active":true,"gradient_roll":0,"blur":3,"mirror":false,"gradient_repeat":1,"gradient_name":"Rainbow","brightness":1,"flip":false},"name":"Wavelength","type":"wavelength(Reactive)","active":true,"isProcessing":false}}' 'http://192.168.0.87:8888/api/devices/wled/effects'
