use std::collections::HashSet;
use std::fs;

const TILES: [[(i32, i32); 5]; 5] = [
    [(0, 0), (0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 0), (0, 1), (1, 0), (1, 1)],
];

pub fn part1() {
    println!("part1: {}", solve(2022))
}
pub fn part2() {
    println!("part2: {}", solve(1_000_000_000_000))
}

fn solve(goal: u64) -> u64 {
    let data = fs::read_to_string("../Inputs/InputDay17.txt").expect("Unable to read file");
    let dirs = data.chars().collect();
    let mut board = HashSet::from_iter((0..7).map(|x| (x, -1)));
    let mut dct = vec![];
    let mut starting_pos = 3;
    let mut d = 0;
    for piece_num in 0..goal as u64 {
        if let Some(res) = fall_piece(
            piece_num,
            &mut board,
            &mut dct,
            &mut starting_pos,
            &mut d,
            goal,
            &dirs,
        ) {
            return res;
        }
    }
    unreachable!()
}

fn place_tile(
    board: &mut HashSet<(i32, i32)>,
    tile: [(i32, i32); 5],
    offset_x: i32,
    offset_y: i32,
) {
    for (x, y) in tile {
        board.insert((x + offset_x, y + offset_y));
    }
}

fn is_valid(
    board: &HashSet<(i32, i32)>,
    tile: [(i32, i32); 5],
    offset_x: i32,
    offset_y: i32,
) -> bool {
    return tile
        .iter()
        .all(|(x, y)| !board.contains(&(x + offset_x, y + offset_y)));
}

fn can_skip(
    piece_num: u64,
    board: &mut HashSet<(i32, i32)>,
    dct: &mut Vec<(i32, usize)>,
    starting_pos: &mut i32,
    d: &mut usize,
    goal: u64,
    dirs: &Vec<char>,
) -> Option<u64> {
    if piece_num != 0 && piece_num % 3 == 0 {
        let moves = piece_num as usize / 3;
        let (height_at_2thirds, d_pos) = dct[moves * 2];
        let (height_at_third, d_pos2) = dct[moves];
        let cur_height = *starting_pos - 3;
        let height_at_repeat = cur_height;
        if d_pos == d_pos2
            && d_pos == *d % dirs.len() as usize
            && cur_height - height_at_2thirds == height_at_2thirds - height_at_third
        {
            let growth = cur_height - height_at_2thirds;
            let res = height_at_third as u64 + growth as u64 * (goal / moves as u64 - 1);
            for i in 1..goal % moves as u64 {
                fall_piece(piece_num + i, board, dct, starting_pos, d, goal, dirs);
            }
            return Some(res + *starting_pos as u64 - 3 - height_at_repeat as u64);
        }
    }
    None
}

fn fall_piece(
    piece_num: u64,
    board: &mut HashSet<(i32, i32)>,
    dct: &mut Vec<(i32, usize)>,
    starting_pos: &mut i32,
    d: &mut usize,
    goal: u64,
    dirs: &Vec<char>,
) -> Option<u64> {
    let tile = TILES[(piece_num % TILES.len() as u64) as usize];
    let biggest_x = tile.iter().map(|&p| p.0).max().unwrap();
    let (mut off_set_y, mut off_set_x) = (*starting_pos, 2);
    loop {
        if dirs[*d] == '>' {
            if off_set_x + biggest_x < 6 && is_valid(board, tile, off_set_x + 1, off_set_y) {
                off_set_x += 1;
            }
        } else if off_set_x > 0 && is_valid(board, tile, off_set_x - 1, off_set_y) {
            off_set_x -= 1;
        }

        *d = (*d + 1) % dirs.len();
        if !is_valid(board, tile, off_set_x, off_set_y - 1) {
            place_tile(board, tile, off_set_x, off_set_y);
            *starting_pos =
                (*starting_pos).max(4 + off_set_y + tile.iter().map(|&p| p.1).max().unwrap());
            dct.push((*starting_pos - 3, *d % dirs.len()));
            if let res @ Some(_) = can_skip(piece_num, board, dct, starting_pos, d, goal, dirs) {
                return res;
            }
            return if piece_num as u64 + 1 == goal {
                Some((*starting_pos - 3) as u64)
            } else {
                None
            };
        }
        off_set_y -= 1;
    }
}
