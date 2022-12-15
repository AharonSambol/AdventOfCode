use std::collections::HashSet;
use std::fs;

pub fn part1() {
    solve(true)
}
pub fn part2() {
    solve(false)
}

fn solve(part1: bool) {
    let data = fs::read_to_string("../Inputs/InputDay14.txt").expect("Unable to read file");
    let mut board = HashSet::new();
    let mut max_y = 0;
    for line in data.split('\n') {
        let line: Vec<Vec<usize>> = line
            .split(" -> ")
            .map(|x| x.split(',').map(|v| v.parse::<usize>().unwrap()).collect())
            .collect();
        max_y = max_y.max(line.iter().map(|r| r[1]).max().unwrap());
        for (pair1, pair2) in line.iter().zip(line.iter().skip(1)) {
            let xs = [pair1[0], pair2[0]];
            let ys = [pair1[1], pair2[1]];
            for x in *xs.iter().min().unwrap()..=*xs.iter().max().unwrap() {
                for y in *ys.iter().min().unwrap()..=*ys.iter().max().unwrap() {
                    board.insert((x, y));
                }
            }
        }
    }
    let rocks = board.len();
    let mut path = vec![];
    let mut sand = (500, 0);
    'main_loop: while !(part1 && sand.1 + 1 > max_y) {
        path.push(sand);
        if sand.1 < max_y + 1 {
            for dir in [(0, 1), (-1, 1), (1, 1)] {
                let new_sand = ((sand.0 as i32 + dir.0) as usize, sand.1 + dir.1);
                if !board.contains(&new_sand) {
                    sand = new_sand;
                    continue 'main_loop;
                }
            }
        }
        board.insert(sand);
        if path.len() == 1 {
            break;
        }
        path.pop().unwrap();
        sand = path.pop().unwrap();
    }
    println!("{}", board.len() - rocks)
}
