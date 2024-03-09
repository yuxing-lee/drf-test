let findImageChild = async (node, parent_id) => {
    if (node["id"] == parent_id) {
        return node;
    } else if (node["child"].length == 0) {
        return null;
    }
    for (let child of node["child"]) {
        if (child["id"] == parent_id) {
            return child;
        }
        let result = await findImageChild(child, parent_id);
        if (result) {
            return result;
        }
    }
};

let delImageChild = async (node, delete_id) => {
    let delete_index = -1;
    for (let index in node["child"]) {
        let child = node["child"][index];
        // 找到要刪除的節點
        if (child["id"] == delete_id) {
            delete_index = index;
            break;
        }
    }
    // 若沒找到要刪除的節點則繼續往下找，直到找到為止
    if (delete_index == -1) {
        for (let child of node["child"]) {
            await delImageChild(child, delete_id);
        }
    } else {
        // 刪除所有子節點
        for (let child of node["child"][delete_index]["child"]) {
            await delImageChild(node["child"][delete_index], child["id"]);
        }
        // 刪除節點及畫面
        node["child"].splice(delete_index, 1);
        document.getElementById(`div-${delete_id}`).remove();
    }
};

let syncImageProcessResult = async (root) => {
    let node = JSON.parse(JSON.stringify(root));
    for (let index in node["child"]) {
        node["child"][index] = await syncImageProcessResult(node["child"][index]);
    }
    // set image url
    if (node["id"]) {
        let image = document.getElementById(`image-${node["id"]}`);
        image.src = node["image_url"] + "?" + new Date().getTime();
    }
    return node;
};
