use itertools::Itertools;
use regex::Regex;
use std::collections::HashSet;
use std::process::exit;
use std::sync::Arc;
use std::thread::sleep;
use std::time::Duration;
use std::{fs, thread};

pub fn solve() {
    let data = fs::read_to_string("../Inputs/InputDay15.txt").expect("Unable to read file");
    let mut beacons = HashSet::new();
    let mut sensors = vec![];
    for line in data.split('\n') {
        let (s_x, s_y, b_x, b_y) = Regex::new(r"-?\d+")
            .unwrap()
            .find_iter(line)
            .map(|x| x.as_str().parse::<i32>().unwrap())
            .collect_tuple()
            .unwrap();
        beacons.insert((b_x, b_y));
        sensors.push((s_x, s_y, (s_x - b_x).abs() + (s_y - b_y).abs()));
    }
    println!("part1: {}", part1(&sensors, beacons, 2000000));

    let arc = Arc::new(sensors);
    let threads = 100;
    let portion = 4000000 / threads;
    for i in 0..threads {
        let sensors_pointer = arc.clone();
        let (start, end) = (portion * i, portion * (i + 1));
        thread::spawn(move || {
            for y in start..=end {
                if let Some(res) = part2(&sensors_pointer, y, 0, 4000000) {
                    println!("part2: {res}");
                    exit(0)
                }
            }
        });
    }

    loop {
        sleep(Duration::MAX);
    }
}

fn part1(sensors: &Vec<(i32, i32, i32)>, beacons: HashSet<(i32, i32)>, y: i32) -> i32 {
    let ranges: Vec<(i32, i32)> = sensors
        .iter()
        .filter_map(|(s_x, s_y, r)| {
            let w = *r - (*s_y - y).abs();
            if w > 0 {
                Some((*s_x - w, *s_x + w))
            } else {
                None
            }
        })
        .collect();
    let mut res = 0;
    let mut skip = HashSet::new();
    for (i, (mut r1_start, mut r1_end)) in ranges.iter().enumerate() {
        if skip.contains(&i) {
            continue;
        }
        'lp: loop {
            for (j, (r2_start, r2_end)) in ranges.iter().enumerate().skip(i + 1) {
                if skip.contains(&j) {
                    continue;
                }
                // if the ranges overlap
                if r1_start <= *r2_start && *r2_start <= r1_end
                    || *r2_start <= r1_end && r1_end <= *r2_end
                    || r1_start <= *r2_end && *r2_end <= r1_end
                    || *r2_start <= r1_start && r1_start <= *r2_end
                {
                    (r1_start, r1_end) = (r1_start.min(*r2_start), r1_end.max(*r2_end));
                    skip.insert(j);
                    continue 'lp;
                }
            }
            break;
        }
        res += r1_end - r1_start + 1;
    }
    res - beacons.iter().filter(|(_, y_pos)| *y_pos == y).count() as i32
}

fn part2(sensors: &Arc<Vec<(i32, i32, i32)>>, y: i32, mut start: i32, end: i32) -> Option<i64> {
    let ranges = sensors
        .iter()
        .filter_map(|(s_x, s_y, r)| {
            let w = r - (s_y - y).abs();
            if w > 0 && s_x - w <= end {
                Some((s_x - w, s_x + w))
            } else {
                None
            }
        })
        .sorted_by_key(|(x, _)| *x);
    for (r1_start, r1_end) in ranges {
        if r1_start <= start {
            start = r1_end.max(start);
        } else {
            return Some((r1_start - 1) as i64 * 4000000 + y as i64);
        }
    }
    None
}
