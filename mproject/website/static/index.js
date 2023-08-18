function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }

  function deleteCab(cabId) {
    fetch("/delete-cab", {
      method: "POST",
      body: JSON.stringify({ cabId: cabId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }
  