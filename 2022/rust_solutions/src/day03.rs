use itertools::Itertools;
use std::collections::{HashMap, HashSet};
use std::fs;

pub fn solve() {
    let data = fs::read_to_string("../Inputs/InputDay03.txt").expect("Unable to read file");
    let alphabet: HashMap<char, usize> = HashMap::from_iter(
        ('a'..='z')
            .chain('A'..='Z')
            .enumerate()
            .map(|(i, c)| (c, i + 1)),
    );
    let res1: usize = data
        .split('\n')
        .map(|line| {
            let (a, b) = line.split_at(line.len() / 2);
            let a: HashSet<char> = HashSet::from_iter(a.chars());
            let b: HashSet<char> = HashSet::from_iter(b.chars());
            let c = a.intersection(&b).next().unwrap();
            alphabet[c]
        })
        .sum();

    let res2: usize = data
        .split('\n')
        .map(|x| HashSet::from_iter(x.chars()))
        .chunks(3)
        .into_iter()
        .map(|mut sets| {
            let mut same: HashSet<char> = sets.next().unwrap();
            sets.for_each(|other| same.retain(|x| other.contains(&x)));
            alphabet[same.iter().next().unwrap()]
        })
        .sum();

    println!("part1: {}\npart2: {}", res1, res2)
}
