import time
#VERSION %r v1.26rc8
# PIF HARD RESET
time.sleep(1e-3)
spi.spiw(0xfe,0x00)
spi.spiw(0xfe,0x01)
time.sleep(1e-3)
spi.spiw(0xfe,0x00)
time.sleep(400e-6)
# GENERIC: begin
spi.spiw(0xff,0x00)
spi.spiw(0x10,0x00)
spi.spiw(0x24,0xea)
spi.spiw(0x25,0x00)
spi.spiw(0x26,0x10)
spi.spiw(0x27,0x00)
spi.spiw(0x28,0x00)
spi.spiw(0x29,0x01)
spi.spiw(0x19,0x00)
spi.spiw(0x11,0x00)
spi.spiw(0x12,0x00)
spi.spiw(0x13,0x08)
spi.spiw(0x14,0x01)
spi.spiw(0x15,0x00)
spi.spiw(0x16,0x00)
spi.spiw(0x17,0x80)
spi.spiw(0x18,0x00)
spi.spiw(0x23,0x01)
spi.spiw(0x2a,0x00)
spi.spiw(0x2c,0x02)
spi.spiw(0x2d,0xa8)
spi.spiw(0x2e,0x90)
spi.spiw(0x2f,0x01)
# GENERIC: end

# NVM Copy to NVM Update
spi.spiw(0x0f,0x00)
spi.spiw(0x0f,0x30)
spi.spiw(0x0f,0x00)
time.sleep(10e-6)
# FORCE POWER UP
spi.spiw(0xe0,0x7f)
spi.spiw(0xe1,0x7f)
time.sleep(400e-6)
# Proceed to Loop Lock
spi.spiw(0x0f,0x00)
spi.spiw(0x0f,0xd8)
spi.spiw(0x0f,0x00)
# INPUT_SYS: begin
spi.spiw(0xff,0x02)
spi.spiw(0x10,0x02)
spi.spiw(0x11,0x80)
spi.spiw(0x12,0x00)
spi.spiw(0x13,0x00)
spi.spiw(0x14,0x00)
spi.spiw(0x15,0x00)
spi.spiw(0x16,0xff)
spi.spiw(0x17,0xff)
spi.spiw(0x18,0xff)
spi.spiw(0x19,0xff)
spi.spiw(0x1a,0x10)
spi.spiw(0x1b,0x4c)
spi.spiw(0x1c,0xcc)
spi.spiw(0x1d,0xcc)
spi.spiw(0x11,0x80)
spi.spiw(0x21,0x00)
spi.spiw(0x1e,0x62)
spi.spiw(0x1f,0x15)
spi.spiw(0x2e,0x21)
spi.spiw(0x2f,0x15)
spi.spiw(0x3e,0xf1)
spi.spiw(0x3f,0x15)
spi.spiw(0x4e,0x11)
spi.spiw(0x4f,0x15)
# INPUT_SYS: end

# NVM Copy to NVM Update
spi.spiw(0x0f,0x00)
spi.spiw(0x0f,0x30)
spi.spiw(0x0f,0x00)
time.sleep(10e-6)
# Proceed to Loop Lock
spi.spiw(0x0f,0x00)
spi.spiw(0x0f,0xd8)
spi.spiw(0x0f,0x00)
time.sleep(6e-3)
# CLOCK_MON: begin
spi.spiw(0xff,0x01)
spi.spiw(0x11,0x00)
spi.spiw(0x12,0x00)
spi.spiw(0x13,0x01)
spi.spiw(0x14,0xf2)
spi.spiw(0x15,0x00)
spi.spiw(0x16,0x01)
spi.spiw(0x17,0xf2)
spi.spiw(0x18,0x00)
spi.spiw(0x19,0x01)
spi.spiw(0x1a,0xf3)
spi.spiw(0x1b,0x00)
spi.spiw(0x1c,0x00)
spi.spiw(0x1d,0x62)
spi.spiw(0x1e,0x00)
spi.spiw(0x1f,0x01)
spi.spiw(0x20,0x8e)
spi.spiw(0x21,0x00)
spi.spiw(0x22,0x01)
spi.spiw(0x23,0x8e)
spi.spiw(0x24,0x00)
spi.spiw(0x25,0x01)
spi.spiw(0x26,0x8f)
spi.spiw(0x27,0x00)
spi.spiw(0x28,0x00)
spi.spiw(0x29,0x4e)
spi.spiw(0x46,0x00)
spi.spiw(0x47,0x77)
spi.spiw(0x48,0x77)
spi.spiw(0x2a,0x00)
spi.spiw(0x2b,0x04)
spi.spiw(0x2c,0x00)
spi.spiw(0x2d,0x00)
spi.spiw(0x2e,0x06)
spi.spiw(0x2f,0x06)
spi.spiw(0x30,0x46)
spi.spiw(0x31,0x00)
spi.spiw(0x32,0x04)
spi.spiw(0x33,0x04)
spi.spiw(0x34,0x04)
spi.spiw(0x35,0x04)
spi.spiw(0x36,0x77)
spi.spiw(0x37,0x77)
spi.spiw(0x38,0x99)
spi.spiw(0x39,0x99)
spi.spiw(0x3a,0x60)
spi.spiw(0x3b,0x00)
spi.spiw(0x3c,0x00)
spi.spiw(0x3d,0x60)
spi.spiw(0x3e,0x00)
spi.spiw(0x3f,0x00)
spi.spiw(0x40,0x60)
spi.spiw(0x41,0x00)
spi.spiw(0x42,0x00)
spi.spiw(0x43,0x4c)
spi.spiw(0x44,0xcc)
spi.spiw(0x45,0xcc)
spi.spiw(0x4c,0x05)
spi.spiw(0x4d,0x05)
spi.spiw(0x4e,0x05)
spi.spiw(0x4f,0x05)
spi.spiw(0x49,0x00)
spi.spiw(0x4a,0x00)
spi.spiw(0x4b,0x00)
# CLOCK_MON: end

# NVM Copy to NVM Update
spi.spiw(0x0f,0x00)
spi.spiw(0x0f,0x30)
spi.spiw(0x0f,0x00)
time.sleep(10e-6)
# Proceed to Loop Lock
spi.spiw(0x0f,0x00)
spi.spiw(0x0f,0xd8)
spi.spiw(0x0f,0x00)
# OUT_SYS: begin
spi.spiw(0xff,0x03)
spi.spiw(0x10,0x00)
spi.spiw(0x11,0x00)
spi.spiw(0x12,0x16)
spi.spiw(0x13,0x0f)
spi.spiw(0x14,0x00)
spi.spiw(0x15,0x20)
spi.spiw(0x17,0x00)
spi.spiw(0x18,0x00)
spi.spiw(0x19,0x00)
spi.spiw(0x1a,0x16)
spi.spiw(0x1b,0x0f)
spi.spiw(0x1c,0x00)
spi.spiw(0x1d,0x20)
spi.spiw(0x1f,0x00)
spi.spiw(0x20,0x00)
spi.spiw(0x21,0x00)
spi.spiw(0x22,0x17)
spi.spiw(0x23,0x0f)
spi.spiw(0x24,0x00)
spi.spiw(0x25,0x20)
spi.spiw(0x27,0x00)
spi.spiw(0x28,0x00)
spi.spiw(0x29,0x00)
spi.spiw(0x2a,0x17)
spi.spiw(0x2b,0x0f)
spi.spiw(0x2c,0x00)
spi.spiw(0x2d,0x20)
spi.spiw(0x2f,0x00)
spi.spiw(0x30,0x00)
spi.spiw(0x31,0x00)
spi.spiw(0x32,0x18)
spi.spiw(0x33,0x0f)
spi.spiw(0x34,0x00)
spi.spiw(0x35,0x20)
spi.spiw(0x37,0x00)
spi.spiw(0x38,0x00)
spi.spiw(0x39,0x00)
spi.spiw(0x3a,0x18)
spi.spiw(0x3b,0x0f)
spi.spiw(0x3c,0x00)
spi.spiw(0x3d,0x20)
spi.spiw(0x3f,0x00)
spi.spiw(0x40,0x00)
spi.spiw(0x41,0x00)
spi.spiw(0x42,0x19)
spi.spiw(0x43,0x0f)
spi.spiw(0x44,0x00)
spi.spiw(0x45,0x20)
spi.spiw(0x47,0x00)
spi.spiw(0x48,0x00)
spi.spiw(0x49,0x00)
spi.spiw(0x4a,0x19)
spi.spiw(0x4b,0x0f)
spi.spiw(0x4c,0x00)
spi.spiw(0x4d,0x20)
spi.spiw(0x4f,0x00)
spi.spiw(0x50,0x00)
spi.spiw(0x51,0x00)
spi.spiw(0x52,0x19)
spi.spiw(0x53,0x0f)
spi.spiw(0x54,0x00)
spi.spiw(0x55,0x20)
spi.spiw(0x57,0x00)
spi.spiw(0x63,0x0f)
spi.spiw(0x64,0x00)
spi.spiw(0x65,0x20)
spi.spiw(0x67,0x00)
spi.spiw(0x60,0x00)
spi.spiw(0x61,0x00)
spi.spiw(0x62,0x16)
# OUT_SYS: end

# NVM Copy to NVM Update
spi.spiw(0x0f,0x00)
spi.spiw(0x0f,0x30)
spi.spiw(0x0f,0x00)
time.sleep(10e-6)
# Proceed to Loop Lock
spi.spiw(0x0f,0x00)
spi.spiw(0x0f,0xd8)
spi.spiw(0x0f,0x00)
# PLLA: begin
spi.spiw(0xff,0x0a)
spi.spiw(0x10,0xb0)
spi.spiw(0x11,0x57)
spi.spiw(0x12,0xec)
spi.spiw(0x13,0xeb)
spi.spiw(0x14,0x24)
spi.spiw(0x15,0xa3)
spi.spiw(0x19,0x4d)
spi.spiw(0x2d,0x5f)
spi.spiw(0x2e,0x2e)
spi.spiw(0x17,0x51)
spi.spiw(0x18,0x80)
spi.spiw(0x1a,0x55)
spi.spiw(0x1b,0x55)
spi.spiw(0x1c,0x61)
spi.spiw(0x1d,0x1a)
spi.spiw(0x1e,0x06)
spi.spiw(0x1f,0x80)
spi.spiw(0x20,0xff)
spi.spiw(0x21,0xff)
spi.spiw(0x22,0xff)
spi.spiw(0x23,0x7f)
spi.spiw(0x24,0xfe)
spi.spiw(0x25,0xff)
spi.spiw(0x26,0xff)
spi.spiw(0x27,0xff)
spi.spiw(0x16,0xdf)
spi.spiw(0x28,0x23)
spi.spiw(0x2b,0x66)
spi.spiw(0x2c,0xbe)
spi.spiw(0x29,0x0f)
spi.spiw(0x2a,0x34)
spi.spiw(0x2f,0x02)
# PLLA: end

# NVM Copy to NVM Update
spi.spiw(0x0f,0x00)
spi.spiw(0x0f,0x30)
spi.spiw(0x0f,0x00)
time.sleep(10e-6)
# Proceed to Loop Lock
spi.spiw(0x0f,0x00)
spi.spiw(0x0f,0xd8)
spi.spiw(0x0f,0x00)
# PLLB: begin
spi.spiw(0xff,0x0b)
spi.spiw(0x10,0xb0)
spi.spiw(0x11,0x57)
spi.spiw(0x12,0xec)
spi.spiw(0x13,0xcb)
spi.spiw(0x14,0x24)
spi.spiw(0x15,0xa3)
spi.spiw(0x19,0x4d)
spi.spiw(0x2d,0x5f)
spi.spiw(0x2e,0x2e)
spi.spiw(0x17,0x4e)
spi.spiw(0x18,0x86)
spi.spiw(0x1a,0x00)
spi.spiw(0x1b,0x00)
spi.spiw(0x1c,0x20)
spi.spiw(0x1d,0xdc)
spi.spiw(0x1e,0x05)
spi.spiw(0x1f,0x80)
spi.spiw(0x20,0x00)
spi.spiw(0x21,0x00)
spi.spiw(0x22,0x00)
spi.spiw(0x23,0x00)
spi.spiw(0x24,0xff)
spi.spiw(0x25,0xff)
spi.spiw(0x26,0xff)
spi.spiw(0x27,0xff)
spi.spiw(0x16,0xdf)
spi.spiw(0x28,0x0c)
spi.spiw(0x2b,0x66)
spi.spiw(0x2c,0xbe)
spi.spiw(0x29,0x0f)
spi.spiw(0x2a,0x34)
spi.spiw(0x2f,0x02)
# PLLB: end

# NVM Copy to NVM Update
spi.spiw(0x0f,0x00)
spi.spiw(0x0f,0x30)
spi.spiw(0x0f,0x00)
time.sleep(10e-6)
# Proceed to Loop Lock
spi.spiw(0x0f,0x00)
spi.spiw(0x0f,0xd8)
spi.spiw(0x0f,0x00)
# PLLC: begin
spi.spiw(0xff,0x0c)
spi.spiw(0x10,0xb0)
spi.spiw(0x11,0x57)
spi.spiw(0x12,0xec)
spi.spiw(0x13,0xcb)
spi.spiw(0x14,0x24)
spi.spiw(0x15,0xa3)
spi.spiw(0x19,0x4d)
spi.spiw(0x2d,0x5f)
spi.spiw(0x2e,0x2e)
spi.spiw(0x17,0x4b)
spi.spiw(0x18,0x88)
spi.spiw(0x1a,0xaa)
spi.spiw(0x1b,0xaa)
spi.spiw(0x1c,0xde)
spi.spiw(0x1d,0x9d)
spi.spiw(0x1e,0x05)
spi.spiw(0x1f,0x80)
spi.spiw(0x20,0xff)
spi.spiw(0x21,0xff)
spi.spiw(0x22,0xff)
spi.spiw(0x23,0x7f)
spi.spiw(0x24,0xfe)
spi.spiw(0x25,0xff)
spi.spiw(0x26,0xff)
spi.spiw(0x27,0xff)
spi.spiw(0x16,0xdf)
spi.spiw(0x28,0x0c)
spi.spiw(0x2b,0x66)
spi.spiw(0x2c,0xbe)
spi.spiw(0x29,0x0f)
spi.spiw(0x2a,0x34)
spi.spiw(0x2f,0x02)
# PLLC: end

# NVM Copy to NVM Update
spi.spiw(0x0f,0x00)
spi.spiw(0x0f,0x30)
spi.spiw(0x0f,0x00)
time.sleep(10e-6)
# Proceed to Loop Lock
spi.spiw(0x0f,0x00)
spi.spiw(0x0f,0xd8)
spi.spiw(0x0f,0x00)
# PLLD: begin
spi.spiw(0xff,0x0d)
spi.spiw(0x10,0x90)
spi.spiw(0x11,0x57)
spi.spiw(0x12,0xec)
spi.spiw(0x13,0xcb)
spi.spiw(0x14,0x24)
spi.spiw(0x15,0xa3)
spi.spiw(0x19,0x4d)
spi.spiw(0x2d,0x5f)
spi.spiw(0x2e,0x2e)
spi.spiw(0x17,0x48)
spi.spiw(0x18,0x8a)
spi.spiw(0x1a,0x55)
spi.spiw(0x1b,0x55)
spi.spiw(0x1c,0x9d)
spi.spiw(0x1d,0x5f)
spi.spiw(0x1e,0x05)
spi.spiw(0x1f,0x80)
spi.spiw(0x20,0x00)
spi.spiw(0x21,0x00)
spi.spiw(0x22,0x00)
spi.spiw(0x23,0x00)
spi.spiw(0x24,0xff)
spi.spiw(0x25,0xff)
spi.spiw(0x26,0xff)
spi.spiw(0x27,0xff)
spi.spiw(0x16,0xdf)
spi.spiw(0x28,0x23)
spi.spiw(0x2b,0x66)
spi.spiw(0x2c,0xbe)
spi.spiw(0x29,0x0f)
spi.spiw(0x2a,0x34)
spi.spiw(0x2f,0x02)
# PLLD: end

# NVM Copy to NVM Update
spi.spiw(0x0f,0x00)
spi.spiw(0x0f,0x30)
spi.spiw(0x0f,0x00)
time.sleep(10e-6)
# Proceed to Loop Lock
spi.spiw(0x0f,0x00)
spi.spiw(0x0f,0xd8)
spi.spiw(0x0f,0x00)
