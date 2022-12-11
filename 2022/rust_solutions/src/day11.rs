use regex::Regex;
use std::fs;

const PART1: bool = true;

pub fn solve() {
    let data = fs::read_to_string("../Inputs/InputDay11.txt").expect("Unable to read file");
    let data = data.split("\n\n");
    let mut monkeys: Vec<Monkey> = data
        .map(|x| {
            Regex::new(r"\n\s*")
                .unwrap()
                .split(x)
                .skip(1)
                .collect::<Vec<&str>>()
        })
        .map(|monk| Monkey {
            items: Regex::new(r"\d+")
                .unwrap()
                .find_iter(monk[0])
                .map(|x| x.as_str().parse::<usize>().unwrap())
                .collect(),
            op: monk[1]
                .split("= ")
                .nth(1)
                .unwrap()
                .split(' ')
                .map(|x| String::from(x))
                .collect(),
            test: monk[2]
                .strip_prefix("Test: divisible by ")
                .unwrap()
                .parse::<usize>()
                .unwrap(),
            t: monk[3].split(' ').last().unwrap().parse::<i32>().unwrap(),
            f: monk[4].split(' ').last().unwrap().parse::<i32>().unwrap(),
            business: 0,
        })
        .collect();
    let prod = monkeys.iter().map(|x| x.test).reduce(|x, y| x * y).unwrap();
    for _ in 0..(if PART1 { 20 } else { 10000 }) {
        let ln = monkeys.len();
        for i in 0..ln {
            monkeys[i].business += monkeys[i].items.len();
            for item in monkeys[i].items.clone() {
                let monkey = &mut monkeys[i];
                let vals = [&monkey.op[0], &monkey.op[2]].map(|x| match x.as_str() {
                    "old" => item,
                    _ => x.parse().unwrap(),
                });
                let mut new = match monkey.op[1].as_str() {
                    "+" => vals.iter().sum(),
                    "*" => vals[0] * vals[1],
                    _ => unreachable!(),
                };
                if PART1 {
                    new /= 3;
                }
                let (test, t, f) = (monkey.test, monkey.t, monkey.f);
                monkeys[if new % test == 0 { t } else { f } as usize]
                    .items
                    .push(new as usize % prod);
            }
            monkeys[i].items.clear();
        }
    }
    let mut business: Vec<usize> = monkeys.iter().map(|x| x.business).collect();
    let m1 = *business.iter().max().unwrap();
    if let Some(index) = business.iter().position(|x| *x == m1) {
        business.swap_remove(index);
    }
    println!("{}", m1 * business.iter().max().unwrap())
}

struct Monkey {
    items: Vec<usize>,
    op: Vec<String>,
    test: usize,
    t: i32,
    f: i32,
    business: usize,
}
