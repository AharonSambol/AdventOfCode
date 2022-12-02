use std::fs;


pub fn part1() {
    let data = fs::read_to_string("../Inputs/InputDay01.txt").expect("Unable to read file");
    println!("{}", data.split("\n\n")
        .map(|chunk| chunk.split('\n').map(|line| line.parse::<u32>().unwrap()).sum::<u32>())
        .max()
        .unwrap())
}

pub fn part2() {
    let data = fs::read_to_string("../Inputs/InputDay01.txt").expect("Unable to read file");
    let mut mx = [0, 0, 0, 0];
    data.split("\n\n")
        .map(|chunk| chunk.split('\n').map(|line| line.parse::<u32>().unwrap()).sum())
        .for_each(|elf| {
            let mut i = 1;
            while i < 4 && elf > mx[i] {
                mx[i - 1] = mx[i];
                i += 1;
            }
            mx[i - 1] = elf;
        });
    println!("{}", mx.iter().skip(1).sum::<u32>())
}
