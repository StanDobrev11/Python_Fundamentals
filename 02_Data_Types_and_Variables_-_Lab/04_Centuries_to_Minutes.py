centuries = int(input())

years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f"{centuries:.0f} centuries = "
      f"{years:.0f} years = "
      f"{days:.0f} days = "
      f"{hours:.0f} hours = "
      f"{minutes:.0f} minutes")
