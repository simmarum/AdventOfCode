import math
from collections import defaultdict
import bisect


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def read_asteroids(inp):
    asteroids = set()
    for y, line in enumerate(inp):
        for x, elem in enumerate(line):
            if elem == '#':
                asteroids.add(complex(x, y))
    return asteroids


def find_visible(asteroids):
    max_in_sight = 0
    max_in_sight_asteroid = None
    for asteroid in asteroids:
        sight_unique = set()
        for asteroid_visible in asteroids:
            radiant = math.atan2(
                (asteroid_visible.imag - asteroid.imag),
                (asteroid_visible.real - asteroid.real)
            )

            sight_unique.add(radiant)
        if len(sight_unique) > max_in_sight:

            max_in_sight = len(sight_unique)
            max_in_sight_asteroid = asteroid
    return max_in_sight, max_in_sight_asteroid


def part_1(inp):
    asteroids = read_asteroids(inp)
    max_in_sight, _ = find_visible(asteroids)
    return max_in_sight


def vaporize_in_circle(asteroids, laser_asteroid, hit_number):
    sight_x_ray = defaultdict(list)
    asteroid_cnt = 0
    while asteroid_cnt < hit_number:
        for asteroid_visible in asteroids:
            if laser_asteroid == asteroid_visible:
                continue
            radiant = math.atan2(
                (asteroid_visible.imag - laser_asteroid.imag),
                (asteroid_visible.real - laser_asteroid.real)
            )
            radiant = radiant + 2 * math.pi if radiant < 0 else radiant
            radiant = (radiant + (1 / 2) * math.pi) % (2 * math.pi)
            dist = (asteroid_visible.imag - laser_asteroid.imag)**2 + \
                (asteroid_visible.real - laser_asteroid.real)**2
            bisect.insort(sight_x_ray[radiant], (dist, asteroid_visible))
        for next_radiant in sorted(sight_x_ray.keys()):
            _, asteroid_to_hit = sight_x_ray[next_radiant].pop(0)
            asteroid_cnt += 1
            if asteroid_cnt == hit_number:
                return int(asteroid_to_hit.real) * 100 + \
                    int(asteroid_to_hit.imag)
            if not sight_x_ray[next_radiant]:
                del sight_x_ray[next_radiant]


def part_2(inp):
    asteroids = read_asteroids(inp)
    _, laser_asteroid = find_visible(asteroids)
    asteroid_on_hit = vaporize_in_circle(asteroids, laser_asteroid, 200)
    return asteroid_on_hit


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
