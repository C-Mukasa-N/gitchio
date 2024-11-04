using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TaskClickHandler : MonoBehaviour
{
    public Task task; 
    public Routine parentRoutine; // routine parente

    void Start()
    {
        // Trouver le composant Routine parente
        parentRoutine = GetComponentInParent<Routine>();
    }

    void OnMouseDown()
    {
        // Inverser l'état de la tâche
        task.isDone = !task.isDone;

        // update la couleur de la routine
        UpdateRoutineColor();
    }

    public void UpdateRoutineColor()
    {
        if (parentRoutine != null)
        {
            // Logique pour changer la couleur de la routine
            int completedTasks = 0;
            foreach (Task t in parentRoutine.GetTasks())
            {
                if (t.isDone)
                {
                    completedTasks++;
                }
            }

            // Déterminer la couleur de la routine
            if (completedTasks == parentRoutine.GetTasks().Count)
            {
                parentRoutine.SetColor(Routine.RoutineColor.Green);
            }
            else if (completedTasks > 0)
            {
                parentRoutine.SetColor(Routine.RoutineColor.Orange);
            }
            else
            {
                parentRoutine.SetColor(Routine.RoutineColor.Red);
            }
        }
    }
}