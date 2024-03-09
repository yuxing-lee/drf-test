let uploadImageEvent = async (event) => {
    event.preventDefault();
    const form_data = new FormData(event.target);
    if (document.getElementById("image-input").files.length == 0) {
        return;
    }
    let data = await uploadImageApi(form_data);
    /* Append to container */
    let image_container = document.getElementById("image-container");
    image_container.innerHTML = "";
    let image = await generateImageBox(0, 0, "origin-image", data["image_url"]);
    image_container.appendChild(image);
    root = {
        id: 0,
        image_url: data["image_url"],
        function: "",
        params: {},
        changed: false,
        child: [],
    };
};

let imageProcessEvent = async (event) => {
    event.preventDefault();
    let data = await imageProcessApi(JSON.stringify(root));
    root = await syncImageProcessResult(data);
};

let openImageParamsEvent = async (event) => {
    let name_list = event.target.id.split("-");
    let id = parseInt(name_list[1]);
    // generate node data
    let node = await findImageChild(root, id);
    let div_params = await generateParams(node)
    // Append to container
    let param_container = document.getElementById("param-container");
    param_container.innerHTML = "";
    if (current_id == id) {
        current_id = -1;
        param_container.style.display = "none";
        return;
    } else {
        current_id = id;
        param_container.style.display = "initial";
    }
    if (node["id"] != 0) {
        param_container.appendChild(div_params);
    }
};

let paramChangeEvent = async (event) => {
    let name_list = event.target.id.split("-");
    let parent_id = parseInt(name_list[name_list.length - 1]);
    let node = await findImageChild(root, parent_id);
    node["params"][name_list[0]] = parseInt(event.target.value);
};

let delImageChildEvent = async (event) => {
    let name_list = event.target.name.split("-");
    let parent_id = parseInt(name_list[1]);
    await delImageChild(root, parent_id);
};

let clearImageEvent = (event) => {
    document.getElementById("image-container").innerHTML = "";
    document.getElementById("param-container").innerHTML = "";
    document.getElementById("param-container").style.display = "none";
    document.getElementById("image-process").reset();
    document.getElementById("upload-image").reset();
    root = {};
    counter = 1;
    current_id = -1;
};
