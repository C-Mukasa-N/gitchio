using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class menuRoutine : MonoBehaviour
{
    public GameObject panel;
    void Start()
    {
        // Masquer le menu au démarrage
        if (panel != null)
	    {
		    panel.SetActive(false);
	    }
    }
    void OnMouseDown()
    {
        // Lorsque l'objet est cliqué, afficher/masquer le menu
        if (panel != null)
	    {
		    bool isActive = panel.activeSelf;
            panel.SetActive(!isActive);
	    }
    }
}