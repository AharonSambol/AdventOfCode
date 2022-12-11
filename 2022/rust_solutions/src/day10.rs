use std::fs;

pub fn solve() {
    let data = fs::read_to_string("../Inputs/InputDay10.txt").expect("Unable to read file");
    let (mut x, mut pos, mut c, mut res1) = (1, 0, 0, 0);
    let mut res2 = [[' '; 40]; 6];
    for line in data.split('\n') {
        res1 += tick({c += 1; c}, &mut pos, x, &mut res2);
        if line.starts_with("add") {
            res1 += tick({c += 1; c}, &mut pos, x, &mut res2);
            x += line.split(' ').last().unwrap().parse::<i32>().unwrap();
        }
    }
    println!("{res1}\n{}", res2.map(|x| x.iter().collect::<String>()).join("\n"))
}

fn tick(cycle: i32, crt: &mut usize, x_pos: i32, r2: &mut [[char; 40]; 6]) -> i32 {
    r2[*crt / 40][*crt % 40] = if (x_pos - *crt as i32 % 40).abs() < 2 { '#' } else { '.' };
    *crt += 1;
    (cycle % 40 == 20) as i32 * cycle * x_pos
}