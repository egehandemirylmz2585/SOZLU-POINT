from machine import Pin, ADC, PWM

pot = ADC(Pin(32))
led = PWM(Pin(5))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)


while True:
    led.duty_u16(pot.read_u16())
    print(pot.read())