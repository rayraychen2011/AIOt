import mcu


wi = mcu.wifi()
wi.setup(ap_active=False, sta_active=True)
wi.scan()

if wi.connect("Singular_AI", "Singular#1234"):
    print(f"IP={wi.ip}")
