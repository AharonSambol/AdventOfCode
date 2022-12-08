use std::fs;

pub fn solve() {
    let data = fs::read_to_string("../Inputs/InputDay08.txt").expect("Unable to read file");
    let data: Vec<Vec<i32>> = data.split('\n').map(
        |line| line.chars().map(|c| c.to_digit(10).unwrap() as i32).collect()
    ).collect();
    println!("part1: {}", (0..data.len()).map(|r|
            (0..data[0].len()).map(|c|
                val(&data, r, c, true)
            ).sum::<i32>()
        ).sum::<i32>()
    );
    println!("part2: {}", (0..data.len()).map(|r|
            (0..data[0].len()).map(|c|
                val(&data, r, c, false)
            ).max().unwrap()
        ).max().unwrap()
    );
}

fn val(grid: &Vec<Vec<i32>>, r: usize, c: usize, part1: bool) -> i32 {
    let dirs: Vec<Vec<i32>> = vec![
        grid[r].iter().take(c).map(|a| *a).rev().collect(),
        grid[r].iter().skip(c + 1).map(|a| *a).collect(),
        grid.iter().map(|x| x[c]).take(r).rev().collect(),
        grid.iter().map(|x| x[c]).skip(r + 1).collect(),
    ];
    if part1 {
        (dirs.iter().map(|x| *x.iter().max().unwrap_or(&-1)).min().unwrap() < grid[r][c]) as i32
    } else {
        dirs.iter().map(|dr| len_until_limit(dr, grid[r][c])).reduce(|x, y| x * y).unwrap() as i32
    }
}

fn len_until_limit(lst: &Vec<i32>, limit: i32) -> usize {
    lst.iter().enumerate().filter_map(|(i, x)|
        if *x >= limit { Some(i + 1) } else { None }
    ).next().unwrap_or(lst.len())
}
