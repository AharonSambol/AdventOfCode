use itertools::Itertools;
use regex::Regex;
use std::collections::HashMap;
use std::fs;

pub fn solve() {
    let data = fs::read_to_string("../Inputs/InputDay07.txt").expect("Unable to read file");
    let mut dirs: HashMap<String, usize> = HashMap::new();
    let mut path = vec![];
    let re = Regex::new(r"\n\$ ").unwrap();
    let data = format!("\n{}", data);
    let commands = re.split(data.as_str());
    for cmd in commands {
        if cmd == "cd .." {
            path.pop();
        } else if cmd.starts_with("cd") {
            path.push(cmd.strip_prefix("cd ").unwrap());
        } else {
            let size: usize = cmd
                .split('\n')
                .skip(1)
                .filter_map(|x| x.split(' ').next().unwrap().parse::<usize>().ok())
                .sum();
            for i in 0..path.len() {
                *dirs.entry(path.iter().take(i + 1).join("/")).or_default() += size;
            }
        }
    }
    println!(
        "{}",
        dirs.values().filter(|&x| *x <= 100000usize).sum::<usize>()
    );
    println!(
        "{}",
        dirs.values()
            .filter(|&x| *x >= dirs["/"] - 40000000usize)
            .min()
            .unwrap()
    );
}
