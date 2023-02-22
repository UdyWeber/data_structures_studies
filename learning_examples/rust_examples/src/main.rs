#[derive(Clone)]
struct Node {
    value: i64,
    next: Option<Box<Node>>
}


struct LinkedList {
    head: Option<Box<Node>>,
    length: i64
}

impl LinkedList {
    fn new() -> Self {
        Self {
            head: None,
            length: 1
        }
    }

    fn print_list_items(&self) {
        // With as_ref we can get a reference of what's inside the box
        let mut actual_node =  self.head.as_ref();

        while let Some(node) = actual_node {
            println!("Node Value: {}", node.value);
            actual_node = node.next.as_ref();
        }
    }


    fn append(&mut self, value: i64) {
        let new_node = Some(Box::new(Node {
            value: value,
            next: None
        }));

        let mut out_node = &mut self.head;

        while let Some(node) = out_node {
            out_node = &mut node.next;
        }

        *out_node = new_node;
        self.length += 1;
    }
}


fn main() {
    let mut linked_list = LinkedList::new();
    linked_list.append(5123);
    linked_list.append(2310);
    linked_list.append(53);
    linked_list.print_list_items();
}