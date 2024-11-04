using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FireManager : MonoBehaviour
{
    public List<Pillar> pillars;
    
    void Start()
    {
        // Initialiser la liste des piliers si elle n'est pas déjà peuplée
        if (pillars == null || pillars.Count == 0)
        {
            // Trouver tous les objets de type Pillar dans la scène et les ajouter à la liste
            pillars = new List<Pillar>(FindObjectsOfType<Pillar>());
        }
    }

    void Update()
    {
        foreach (Pillar pillar in pillars)
        {
            UpdatePillarColor(pillar);
        }
    }

    public void UpdatePillarColor(Pillar pillar)
    {
        int greenCount = 0;
        int orangeCount = 0;
        int redCount = 0;

        // Compter le nombre de routines de chaque couleur
        foreach (Routine routine in pillar.GetRoutines())
        {
            switch (routine.GetColor())
            {
                case Routine.RoutineColor.Green:
                    greenCount++;
                    break;
                case Routine.RoutineColor.Orange:
                    orangeCount++;
                    break;
                case Routine.RoutineColor.Red:
                    redCount++;
                    break;
            }
        }

        // Déterminer la couleur majoritaire et mettre à jour le pilier
        if (greenCount > orangeCount && greenCount > redCount)
        {
            pillar.SetFireColor(Pillar.FireColor.Green);
        }
        else if (orangeCount > greenCount && orangeCount > redCount)
        {
            pillar.SetFireColor(Pillar.FireColor.Orange);
        }
        else
        {
            pillar.SetFireColor(Pillar.FireColor.Red);
        }
    }
}
