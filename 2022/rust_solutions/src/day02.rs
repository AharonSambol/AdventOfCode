use std::fs;

pub fn solve() {
    let data = fs::read_to_string("../Inputs/InputDay02.txt").expect("Unable to read file");

    let (mut res1, mut res2) = (0, 0);
    for line in data.split('\n'){
        let o = line.chars().next().unwrap() as u32 - 64;
        let me = line.chars().nth(2).unwrap() as u32 - 87;
        res1 += me +
            3 * (me == o) as u32 +
            6 * (me - 1 == o % 3) as u32;
        res2 += 1 +
            (me == 1) as u32 * (o + 1) % 3 +
            (me == 2) as u32 * (o + 2) +
            (me == 3) as u32 * (o % 3 + 6);
    }
    println!("part1: {}\npart2: {}", res1, res2)
}
