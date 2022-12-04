use std::fs;

pub fn solve() {
    let data = fs::read_to_string("../Inputs/InputDay04.txt").expect("Unable to read file");
    let (mut res1, mut res2) = (0, 0);
    for line in data.lines() {
        let nums = line
            .split(',')
            .map(|x| x.split('-').map(|n| n.parse().unwrap()).collect())
            .collect::<Vec<Vec<usize>>>();

        let (start1, end1, start2, end2) = (nums[0][0], nums[0][1], nums[1][0], nums[1][1]);
        res1 += (start1 <= start2 && end2 <= end1
            || start2 <= start1 && end1 <= end2) as usize;
        res2 += (start1 <= start2 && start2 <= end1
            || start1 <= end2 && end2 <= end1
            || start2 <= start1 && start1 <= end2
            || start2 <= end1 && end1 <= end2) as usize;
    }
    println!("part1: {}\npart2: {}", res1, res2)
}
