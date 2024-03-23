let generateImageBox = async (id, layer, image_name, image_url) => {
    let function_name = "";
    if (id != 0) {
        let node = await findImageChild(root, id);
        function_name = node["function"]
    }
    let div = document.createElement("div");
    div.id = `div-${id}`;
    div.className = "image";
    // Add image
    let img = generateImg(id, image_name, image_url);
    div.appendChild(img);
    // Add image info
    let info_div = document.createElement("div");
    info_div.className = "image-info";
    let label = document.createElement("label");
    label.textContent = function_name;
    let add_button = document.createElement("button");
    add_button.name = `abtn-${id}-${layer + 1}`;
    add_button.innerText = "新增";
    add_button.addEventListener("click", addImageChild);
    let delete_button = document.createElement("button");
    delete_button.name = `dbtn-${id}-${layer + 1}`;
    delete_button.innerText = "刪除";
    delete_button.addEventListener("click", delImageChildEvent);
    info_div.appendChild(label);
    info_div.appendChild(generateFunctionSelector(`function-${id}`));
    info_div.appendChild(add_button);
    info_div.appendChild(delete_button);
    div.appendChild(info_div);
    return div;
};

let generateImg = (id, image_name, image_url) => {
    let img = document.createElement("img");
    img.id = `image-${id}`;
    img.alt = image_name;
    img.src = image_url;
    img.addEventListener("click", openImageParamsEvent);
    return img;
}

let generateFunctionGroup = (label) => {
    let group = document.createElement("optgroup");
    group.label = label
    return group;
};

let generateFunctionOption = (text, value) => {
    let option = document.createElement("option");
    option.text = text;
    option.value = value;
    return option;
};

let generateRange = (id, value, min=0, max=255, step=5) => {
    let input = document.createElement("input");
    input.id = id;
    input.type = "range";
    input.min = min;
    input.max = max;
    input.step = step;
    input.value = value;
    return input;
};
