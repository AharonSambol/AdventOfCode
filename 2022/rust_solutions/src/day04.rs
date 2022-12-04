use regex::Regex;
use std::fs;

pub fn solve() {
    let data = fs::read_to_string("../Inputs/InputDay04.txt").expect("Unable to read file");
    let (mut res1, mut res2) = (0, 0);
    for line in data.lines() {
        let nums: Vec<usize> = Regex::new(r"[,-]")
            .unwrap()
            .split(line)
            .map(|x| x.parse().unwrap())
            .collect();
        let (start1, end1, start2, end2) = (nums[0], nums[1], nums[2], nums[3]);
        res1 += (start1 <= start2 && end2 <= end1 || start2 <= start1 && end1 <= end2) as usize;
        res2 += (start1 <= start2 && start2 <= end1 || start2 <= start1 && start1 <= end2) as usize;
    }
    println!("part1: {}\npart2: {}", res1, res2)
}
