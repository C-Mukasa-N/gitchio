using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class StadeArbre : MonoBehaviour
{
    public enum EtatArbre
    {
        Graine,
        JeunePousse,
        Arbre
    }

    public EtatArbre etatActuel; // L'état actuel de l'arbre
    public float dureeJour = 1.0f; // Durée d'un jour en secondes (5 sec = 1 jour)
    public int jourActuel = 1; // Le jour actuel du cycle
    public int cycleTotal = 30; // Nombre total de jours dans un cycle (30 jours)

    private float tempsEcoule = 0.0f; // Le temps écoulé pour suivre la progression des jours

    // Variables pour stocker les différents modèles d'arbre
    public GameObject grainePrefab;
    public GameObject jeunePoussePrefab;
    public GameObject arbrePrefab;

    // Position et rotation personnalisées pour chaque modèle
    public Vector3 positionGraine;
    public Vector3 rotationGraine;

    public Vector3 positionJeunePousse;
    public Vector3 rotationJeunePousse;

    public Vector3 positionArbre;
    public Vector3 rotationArbre;

    private GameObject arbreActuel; // Référence au modèle d'arbre actuellement actif

    void Start()
    {
        // Initialiser l'arbre à l'état de graine au début du cycle
        etatActuel = EtatArbre.Graine;
        arbreActuel = Instantiate(grainePrefab, positionGraine, Quaternion.Euler(rotationGraine));
    }

    void Update()
    {
        // Incrémenter le temps écoulé
        tempsEcoule += Time.deltaTime;

        // Si un jour (5 secondes) s'est écoulé
        if (tempsEcoule >= dureeJour)
        {
            tempsEcoule = 0.0f; // Réinitialiser le compteur de temps
            jourActuel++; // Incrémenter le jour actuel

            // Si le cycle dépasse 30 jours, réinitialiser le cycle
            if (jourActuel > cycleTotal)
            {
                jourActuel = 1;
            }

            // Changer l'état de l'arbre en fonction du jour
            ChangerEtatArbre();
        }
    }

    void ChangerEtatArbre()
    {
        // Passer de la graine à la jeune pousse au jour 5
        if (jourActuel == 5 && etatActuel == EtatArbre.Graine)
        {
            Destroy(arbreActuel); // Détruire le modèle actuel
            etatActuel = EtatArbre.JeunePousse;
            arbreActuel = Instantiate(jeunePoussePrefab, positionJeunePousse, Quaternion.Euler(rotationJeunePousse)); // Instancier le modèle de jeune pousse
        }

        // Passer de la jeune pousse à l'arbre mature au jour 17
        if (jourActuel == 17 && etatActuel == EtatArbre.JeunePousse)
        {
            Destroy(arbreActuel); // Détruire le modèle actuel
            etatActuel = EtatArbre.Arbre;
            arbreActuel = Instantiate(arbrePrefab, positionArbre, Quaternion.Euler(rotationArbre)); // Instancier le modèle d'arbre mature
        }
    }
}
