let generateImageBox = async (id, layer, image_name, image_url) => {
    let div = document.createElement("div");
    div.id = `div-${id}`;
    div.className = "image";
    let img = generateImg(id, image_name, image_url);
    let add_button = document.createElement("button");
    add_button.name = `abtn-${id}-${layer + 1}`;
    add_button.innerText = "新增";
    add_button.addEventListener("click", addImageChild);
    let delete_button = document.createElement("button");
    delete_button.name = `dbtn-${id}-${layer + 1}`;
    delete_button.innerText = "刪除";
    delete_button.addEventListener("click", delImageChildEvent);
    div.appendChild(img);
    div.appendChild(generateFunctionSelector(`function-${id}`));
    div.appendChild(add_button);
    div.appendChild(delete_button);
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
