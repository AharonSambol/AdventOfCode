use std::collections::HashSet;
use std::fs;

pub fn solve() {
    let data = fs::read_to_string("../Inputs/InputDay09.txt").expect("Unable to read file");
    let mut rope = [(0, 0); 10];
    let (mut visited1, mut visited2) = (HashSet::new(), HashSet::new());

    for line in data.split('\n'){
        let dr = match &line.chars().next().unwrap() {
            'R' => (0, 1), 'L' => (0, -1),
            'D' => (1, 0), 'U' => (-1, 0),
            _ => unreachable!()
        };
        for _ in 0..line.split(' ').nth(1).unwrap().parse::<usize>().unwrap() {
            rope[0] = (rope[0].0 + dr.0, rope[0].1 + dr.1);
            for (k, knot) in rope.clone().iter().enumerate() {
                if k == 0 { continue }
                let diff: [i32; 2] = [rope[k-1].0 - knot.0, rope[k-1].1 - knot.1];
                if diff[0].abs() > 1 || diff[1].abs() > 1 {
                    let diff = diff.map(|x| x / x.abs().max(1));
                    rope[k] = (knot.0 + diff[0], knot.1 + diff[1]);
                }
            }
            visited1.insert(rope[1]);
            visited2.insert(*rope.last().unwrap());
        }
    }
    println!("part1: {}, part2: {}", visited1.len(), visited2.len());
}