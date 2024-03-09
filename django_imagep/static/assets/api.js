let uploadImageApi = async (data) => {
    let response = await fetch("api/image-management/", {
        method: "POST",
        body: data,
    });
    return await response.json();
};

let imageProcessApi = async (data) => {
    let response = await fetch("api/image-process/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: data
    });
    return await response.json();
}
