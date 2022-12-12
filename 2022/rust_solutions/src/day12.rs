use std::collections::{HashSet, VecDeque};
use std::sync::{mpsc, Arc};
use std::{fs, thread};

const PART1: bool = false;

pub fn solve() {
    let data = fs::read_to_string("../Inputs/InputDay12.txt").expect("Unable to read file");
    let mut board: Vec<Vec<usize>> = data
        .split('\n')
        .map(|line| line.chars().map(|x| x as usize).collect())
        .collect();
    let mut start = Pos::default();
    let mut end = (0, 0);
    let mut starts = vec![];
    for (r, row) in board.iter().enumerate() {
        for (c, val) in row.iter().enumerate() {
            if *val == 'S' as usize {
                start = Pos { r, c, count: 0 };
            } else if *val == 'E' as usize {
                end = (r, c);
            } else if *val == 'a' as usize {
                starts.push(Pos { r, c, count: 0 })
            }
        }
    }
    board[start.r][start.c] = 'a' as usize;
    board[end.0][end.1] = 'z' as usize;

    let board_arc = Arc::new(board);

    let res = find_path(
        board_arc.clone(),
        end,
        VecDeque::from([start.clone()]),
        HashSet::from([(start.r, start.c)]),
    );
    println!("part1: {res}");

    let mut rxs = vec![];
    for start in starts {
        let (tx, rx) = mpsc::channel();
        let arc = board_arc.clone();
        thread::spawn(move || {
            let res = find_path(
                arc,
                end,
                VecDeque::from([start.clone()]),
                HashSet::from([(start.r, start.c)]),
            );
            tx.send(res).unwrap();
        });
        rxs.push(rx);
    }
    let res = rxs.iter().filter_map(|x| x.recv().ok()).min().unwrap();
    println!("part2: {res}")
}

#[derive(Default, Clone)]
struct Pos {
    r: usize,
    c: usize,
    count: usize,
}

fn find_path(
    board: Arc<Vec<Vec<usize>>>,
    end: (usize, usize),
    mut queue: VecDeque<Pos>,
    mut visited: HashSet<(usize, usize)>,
) -> usize {
    while let Some(pos) = queue.pop_front() {
        for dr in [(0, 1), (0, -1), (1, 0), (-1, 0)] {
            let new_pos = (pos.r as isize + dr.0, pos.c as isize + dr.1);
            if new_pos.0 < 0
                || new_pos.0 >= board.len() as isize
                || new_pos.1 < 0
                || new_pos.1 >= board[0].len() as isize
            {
                continue;
            }
            let new_pos = (new_pos.0 as usize, new_pos.1 as usize);
            if !visited.contains(&new_pos) && board[new_pos.0][new_pos.1] < board[pos.r][pos.c] + 2
            {
                if new_pos == end {
                    return pos.count + 1;
                }
                queue.push_back(Pos {
                    r: new_pos.0,
                    c: new_pos.1,
                    count: pos.count + 1,
                });
                visited.insert(new_pos);
            }
        }
    }
    usize::MAX
}
