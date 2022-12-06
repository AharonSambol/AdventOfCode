use std::collections::HashSet;
use std::fs;

pub fn part1() {
    solve(4)
}
pub fn part2() {
    solve(14)
}

fn solve(ln: usize) {
    let data = fs::read_to_string("../Inputs/InputDay06.txt").expect("Unable to read file");
    let mut data = data.chars().enumerate();
    let mut arr = vec![data.next().unwrap().1; ln];
    for (i, x) in data {
        arr[i % ln] = x;
        if HashSet::<&char>::from_iter(arr.iter()).len() == ln {
            println!("{}", i + 1);
            return;
        }
    }
}
