using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class addRoutine : MonoBehaviour
{
    public class Task
    {
        private string taskName;
        private bool isDone;
    }
    public class Routine
    {
        private enum RoutineColor
        {
            Red,
            Orange,
            Green
        }

    private string routineName;
    private List<Task> tasks;
    private RoutineColor color = RoutineColor.Red;
    
    public RoutineColor GetColor()
		{
		    return color;
		}
    }
}
