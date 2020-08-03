{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Tarea Sofi",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOxH/kc2h/QZ/Xz0fEEKVJj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/GLuarte/TareasX/blob/master/Tarea_Sofi.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RyjDORS8xPSN",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 87
        },
        "outputId": "00b2aa43-03cf-41ae-c0ba-89c321aaa424"
      },
      "source": [
        "!pip install pulp"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: pulp in /usr/local/lib/python3.6/dist-packages (2.2)\n",
            "Requirement already satisfied: amply>=0.1.2 in /usr/local/lib/python3.6/dist-packages (from pulp) (0.1.2)\n",
            "Requirement already satisfied: pyparsing in /usr/local/lib/python3.6/dist-packages (from amply>=0.1.2->pulp) (2.4.7)\n",
            "Requirement already satisfied: docutils>=0.3 in /usr/local/lib/python3.6/dist-packages (from amply>=0.1.2->pulp) (0.15.2)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bJ1zCjujxJHG",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from pulp import *\n",
        "import numpy as np\n"
      ],
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fQNLramZxTFV",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "\n",
        "a=4\n",
        "\n",
        "m=3\n",
        "n=5\n",
        "\n",
        "#equipos_m=[]\n",
        "#for i in range (1,m+1):\n",
        "#  eq='Equipo '+str(i)\n",
        "#  equipos_m.append(eq)\n",
        "\n",
        "#equipos_n=[]\n",
        "#for i in range (m+1,m+n+1):\n",
        "#  eq='Equipo '+str(i)\n",
        "#  equipos_n.append(eq)\n",
        "\n",
        "#equipos=equipos_m+equipos_n\n",
        "\n",
        "fechas=[]\n",
        "for i in range (1,m+n):\n",
        "  eq='Fecha '+str(i)\n",
        "  fechas.append(eq)"
      ],
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_W7PhkXAZXF6",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "equipos_m=['Colo Colo','U de Chile','U Catolica']\n",
        "equipos_n=['Dep Iquique','Cobresal',\"O'Higgins\",'Huachipato','UdeC']\n",
        "equipos=equipos_m+equipos_n"
      ],
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zV9EjRltXnYw",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "torneo=np.zeros((len(fechas),len(equipos),len(equipos)))"
      ],
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JQuA_CONyEBP",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "x=LpVariable.dicts('Partido',\n",
        "                   [(i,j,k) for i in equipos for j in equipos for k in fechas],\n",
        "                   lowBound=0,\n",
        "                   upBound=1,\n",
        "                   cat='Integer'\n",
        "                   )"
      ],
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JdlOCiIt0Kth",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "z=LpProblem('FixtureFutbol',LpMaximize)"
      ],
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3hr4aSPGRz0u",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "z+=lpSum((x[(i,j,k)])for k in fechas for i in equipos for j in equipos)"
      ],
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "d44pTaRuB19_",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# No se puede jugar contra si mismo\n",
        "for i in equipos:\n",
        "  for k in fechas:\n",
        "    z+=x[(i,i,k)]==0"
      ],
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cEsgz-zIJjYC",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#Todos deben jugar contra todos\n",
        "for i in equipos:\n",
        "  for j in equipos:\n",
        "    z+=lpSum((x[(i,j,k)]+x[(j,i,k)])for k in fechas)<=1"
      ],
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IiRQEWz9CXrt",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#cada equipo debe jugar 1 partido x fecha\n",
        "for j in equipos:\n",
        "  for k in fechas:\n",
        "    z+=lpSum((x[(i,j,k)]+x[(j,i,k)]) for i in equipos)==1"
      ],
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XlKovKLkNpG_",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#se deben juar un maximo de 'a' partidos como local\n",
        "for i in equipos:\n",
        "  z+=lpSum((x[(i,j,k)])for k in fechas for j in equipos )<=a"
      ],
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "n7NHgLFJU__5",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#se deben priorizar los clasicos para las ultimas fechas\n",
        "z+=lpSum((x[(i,j,k)]+x[(j,i,k)])for i in equipos_m for j in equipos_m for k in fechas[:3])==0"
      ],
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VuIw5wo3QRQ3",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#Los equipos pequeños deben jugar a lo menos 1 partido de local\n",
        "z+=lpSum((x[(i,j,k)])for i in equipos_n for j in equipos_m for k in fechas)>=1"
      ],
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Tue-qEf_SEoV",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        },
        "outputId": "7474cb08-c2e3-4bb5-df88-d1696fd7d345"
      },
      "source": [
        "z.writeLP('tareaSofi.lp')\n",
        "z.solve()\n",
        "print('status:', LpStatus[z.status])\n",
        "#for v in z.variables():\n",
        "#  print(v.name, v.varValue)\n",
        "print ('FO:',value(z.objective))"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "status: Optimal\n",
            "FO: 28.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "A53LQKpwYKB-",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 745
        },
        "outputId": "eefce4a5-517b-4f4d-b8f6-21c342d5f7e2"
      },
      "source": [
        "for n,k in enumerate(fechas):\n",
        "  for m,j in enumerate(equipos):\n",
        "    for l,i in enumerate(equipos):\n",
        "      torneo[n,l,m]=float(x[(i,j,k)].varValue)\n",
        "      if torneo[n,l,m]==1:\n",
        "        print(k,i,'vs',j)\n",
        "  print('\\n')"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Fecha 1 Dep Iquique vs Cobresal\n",
            "Fecha 1 Colo Colo vs O'Higgins\n",
            "Fecha 1 U de Chile vs Huachipato\n",
            "Fecha 1 U Catolica vs UdeC\n",
            "\n",
            "\n",
            "Fecha 2 Huachipato vs Colo Colo\n",
            "Fecha 2 UdeC vs Dep Iquique\n",
            "Fecha 2 U Catolica vs Cobresal\n",
            "Fecha 2 U de Chile vs O'Higgins\n",
            "\n",
            "\n",
            "Fecha 3 UdeC vs Colo Colo\n",
            "Fecha 3 Cobresal vs U de Chile\n",
            "Fecha 3 O'Higgins vs U Catolica\n",
            "Fecha 3 Dep Iquique vs Huachipato\n",
            "\n",
            "\n",
            "Fecha 4 U Catolica vs Colo Colo\n",
            "Fecha 4 U de Chile vs Dep Iquique\n",
            "Fecha 4 Huachipato vs Cobresal\n",
            "Fecha 4 O'Higgins vs UdeC\n",
            "\n",
            "\n",
            "Fecha 5 Colo Colo vs U de Chile\n",
            "Fecha 5 Dep Iquique vs U Catolica\n",
            "Fecha 5 O'Higgins vs Cobresal\n",
            "Fecha 5 UdeC vs Huachipato\n",
            "\n",
            "\n",
            "Fecha 6 UdeC vs U de Chile\n",
            "Fecha 6 Colo Colo vs Cobresal\n",
            "Fecha 6 Dep Iquique vs O'Higgins\n",
            "Fecha 6 U Catolica vs Huachipato\n",
            "\n",
            "\n",
            "Fecha 7 U de Chile vs U Catolica\n",
            "Fecha 7 Colo Colo vs Dep Iquique\n",
            "Fecha 7 Huachipato vs O'Higgins\n",
            "Fecha 7 Cobresal vs UdeC\n",
            "\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}