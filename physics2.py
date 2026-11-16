"""physics.py - A simple calculator for 5 common physics formulas."""
def velocity(distance, time):
    """v = d / t"""
    return distance / time
def force(mass, acceleration):
    """F = m * a  (Newton's second law)"""
    return mass * acceleration
def kinetic_energy(mass, speed):
    """KE = 1/2 * m * v^2"""
    return 0.5 * mass * speed ** 2
def potential_energy(mass, height, g=9.8):
    """PE = m * g * h"""
    return mass * g * height
def work_done(force_value, distance):
    """W = F * d"""
    return force_value * distance
def main():
    while True:
        print("\n=== Physics Calculator ===")
        print("1. Velocity (v = d / t)")
        print("2. Force (F = m * a)")
        print("3. Kinetic Energy (KE = 1/2 m v^2)")
        print("4. Potential Energy (PE = m g h)")
        print("5. Work Done (W = F * d)")
        choice = input("Choose a formula (1-5): ").strip()
        try:
            if choice == "1":
                d = float(input("Distance (m): "))
                t = float(input("Time (s): "))
                print(f"Velocity = {velocity(d, t):.2f} m/s")
            elif choice == "2":
                m = float(input("Mass (kg): "))
                a = float(input("Acceleration (m/s^2): "))
                print(f"Force = {force(m, a):.2f} N")
            elif choice == "3":
                m = float(input("Mass (kg): "))
                v = float(input("Speed (m/s): "))
                print(f"Kinetic Energy = {kinetic_energy(m, v):.2f} J")
            elif choice == "4":
                m = float(input("Mass (kg): "))
                h = float(input("Height (m): "))
                print(f"Potential Energy = {potential_energy(m, h):.2f} J")
            elif choice == "5":
                f = float(input("Force (N): "))
                d = float(input("Distance (m): "))
                print(f"Work Done = {work_done(f, d):.2f} J")
            else:
                print("Invalid choice. Pick a number from 1 to 5.")
        except ValueError:
            print("Please enter numbers only.")
        except ZeroDivisionError:
            print("Time cannot be zero.")
        again = input("\nDo you want to continue? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()