document.addEventListener('DOMContentLoaded', function () {
    console.log("DOM yüklendi");

    const openContentFormButton = document.getElementById('openContentFormButton');
    const contentFormModal = new bootstrap.Modal(document.getElementById('contentFormModal')); // Bootstrap 4 için uygun
    const editButtons = document.querySelectorAll('.edit-content-button');
    const editFormModal = new bootstrap.Modal(document.getElementById('contentFormModal')); // Bootstrap 4 için uygun
    const editForm = document.getElementById('editContentForm');
    const saveContentButton = document.getElementById('saveContentButton');

    openContentFormButton.addEventListener('click', function () {
        console.log("Add Content butonuna tıklandı");
        contentFormModal.show();
        editForm.reset(); // Formu sıfırla
    });

    editButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            console.log("Düzenleme butonuna tıklandı");
            const contentId = event.target.getAttribute('data-content-id');
            const contentTitle = event.target.getAttribute('data-content-title');
            const contentText = event.target.getAttribute('data-content-text');
            const contentVideo = 'https://www.example.com/video.mp4'; // Örnek video URL'si

            editForm.querySelector('#id_content').value = contentId;
            editForm.querySelector('#id_baslik').value = contentTitle;
            editForm.querySelector('#id_metin').value = contentText;
            editForm.querySelector('#id_video').value = contentVideo;

            editFormModal.show();
        });
    });

    saveContentButton.addEventListener('click', function () {
        console.log("İçerik kaydedildi.");
        // Formu burada kaydetme işlemlerini yapabilirsiniz.
    });
});



