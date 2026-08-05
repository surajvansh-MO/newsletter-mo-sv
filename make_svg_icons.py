import base64

# Professional calendar SVG matching Figma style - #EB5424
calendar_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#EB5424" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>'

# Professional clock SVG matching Figma style - #EB5424  
clock_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#EB5424" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>'

cal_b64 = base64.b64encode(calendar_svg.encode()).decode()
clk_b64 = base64.b64encode(clock_svg.encode()).decode()

print("CAL_B64:")
print(cal_b64)
print()
print("CLK_B64:")
print(clk_b64)
