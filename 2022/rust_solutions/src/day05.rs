use itertools::Itertools;
use std::fs;

pub fn part1() {
    solve(true)
}
pub fn part2() {
    solve(false)
}

fn solve(part1: bool) {
    let data = fs::read_to_string("../Inputs/InputDay05.txt").expect("Unable to read file");
    let (start, moves) = data.split_once("\n\n").unwrap();
    let mut stacks = vec![vec![]; start.split(' ').last().unwrap().parse::<usize>().unwrap()];
    for line in start.split('\n') {
        let chars: Vec<char> = line.chars().collect();
        for i in (0..line.len()).step_by(4) {
            if chars[i] == '[' {
                stacks[i / 4].insert(0, chars[i + 1]);
            }
        }
    }

    for line in moves.split('\n') {
        let parts = line
            .split(' ')
            .filter_map(|x| x.parse::<usize>().ok())
            .collect_tuple();
        let (amount, from, to) = parts.unwrap();
        let len = stacks[from - 1].len();
        let mut to_add = stacks[from - 1].split_off(len - amount);
        if part1 {
            to_add.reverse();
        }
        stacks[to - 1].extend(to_add);
    }
    println!("{}", stacks.iter().map(|x| x.last().unwrap()).join(""))
}
