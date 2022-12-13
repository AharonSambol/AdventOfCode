use itertools::Itertools;
use regex::Regex;
use std::cmp::Ordering;
use std::fs;

pub fn solve() {
    let data = fs::read_to_string("../Inputs/InputDay13.txt").expect("Unable to read file");
    println!(
        "part1: {}",
        data.split("\n\n")
            .enumerate()
            .filter(|(_, lines)| {
                let (line1, line2) = lines
                    .split('\n')
                    .map(|x| serde_json::from_str(x).unwrap())
                    .collect_tuple()
                    .unwrap();
                compare(&line1, &line2) == Ordering::Less
            })
            .map(|(i, _)| i + 1)
            .sum::<usize>()
    );
    let mut packets = Regex::new("\n+")
        .unwrap()
        .split(&data)
        .map(|x| serde_json::from_str(x).unwrap())
        .collect_vec();
    let two = serde_json::to_value([[2]]).unwrap();
    let six = serde_json::to_value([[6]]).unwrap();
    packets.append(&mut vec![two.clone(), six.clone()]);
    packets.sort_by(|x, y| compare(x, y));
    println!(
        "part2: {}",
        (packets.iter().position(|x| *x == two).unwrap() + 1)
            * (packets.iter().position(|x| *x == six).unwrap() + 1)
    );
}
fn compare(v1: &serde_json::Value, v2: &serde_json::Value) -> Ordering {
    let mut v1_lst = vec![];
    let v1_lst = if let Some(v1_num) = v1.as_i64() {
        if let Some(v2_num) = v2.as_i64() {
            return if v1_num == v2_num {
                Ordering::Equal
            } else if v1_num < v2_num {
                Ordering::Less
            } else {
                Ordering::Greater
            };
        }
        v1_lst.push(serde_json::to_value(v1_num).unwrap());
        &v1_lst
    } else {
        v1.as_array().unwrap()
    };
    let mut v2_lst = vec![];
    let v2_lst = if let Some(lst) = v2.as_array() {
        lst
    } else {
        v2_lst.push(serde_json::to_value(v2.as_i64()).unwrap());
        &v2_lst
    };
    for (first, second) in v1_lst.iter().zip(v2_lst) {
        let res = compare(first, second);
        let Ordering::Equal = res else {
            return res;
        };
    }
    if v1_lst.len() == v2_lst.len() {
        Ordering::Equal
    } else if v1_lst.len() < v2_lst.len() {
        Ordering::Less
    } else {
        Ordering::Greater
    }
}
