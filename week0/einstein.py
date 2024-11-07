def energy_from_mass(mass):

  speed_of_light = 3 * 10**8
  energy = mass * speed_of_light**2
  return energy

if __name__ == "__main__":
  mass = int(input("Enter the mass in kilogram: "))
  energy = energy_from_mass(mass)
  print(f"Equivalent energy in joules: {energy}")
