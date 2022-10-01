import matplotlib.pyplot as plt
import numpy as np

def plot(T0, gamma, phi0):
    '''
    Plot a damped harmonic oscillation.
    
    Input
        T0:    Free period(no damping)  (Periode ohne Dämpfung)
        gamma: Damping constant   (Dämpfungskonstante)
        phi0:  Initial amplitude (Angangsamplitude). 
        
    Assumption:
        Initial change of amplitude d(phi0)/dt(t=0)=0.)
        
    '''
    
    t = np.linspace(0, 10, 400)
    if  T0 < 0:
        omega = -T
        f = omega/(2*np.pi)
    elif T0 == 0:
        print("Input error: Period 'T0' must be positive!")
        exit
    else:
        f = 1/T0
        omega = 2*np.pi/T0
    print("Frequenz (ungedämpft) f = {:.2f}, Kreisfrequenz (ungedämpft) ω =  {:.2f}".format(f,omega))
        
    
    fig, ax = plt.subplots()
    radicant = omega**2-gamma**2
    if radicant > 0:
        # Case: damped oscillation or critical damping
        plt.title('Gedämpfte Oszillation für $T_0$={:.2f}, $\gamma$={}, $\phi_0$={}'.format(T0,gamma,phi0))
        Amp = phi0*np.exp(-gamma*t)        
        Phi = Amp*np.cos(np.sqrt(radicant)*t)
        ax.plot(t, Phi)
        
        A_hndl, = ax.plot(t, Amp,'r--',label='Amplitude')
        legend = ax.legend(handles=[A_hndl])
        ax.add_artist(legend)
        ax.plot(t, -Amp,'r--')
    else:
        # Case: overdamped, no oscillation
        plt.title('Kriechfall (keine Oszillation) für $T_0={}, $\gamma$={}, $\phi_0={}'.format(T0,gamma,phi0))
        gamma1=gamma+np.sqrt(-radicant)
        gamma2=gamma-np.sqrt(-radicant)
        Amp1 = phi0*gamma2*np.exp(-gamma1*t)/(gamma1+gamma2)
        Amp2 = phi0*gamma1*np.exp(-gamma2*t)/(gamma1+gamma2)
        Phi = Amp1 + Amp2
        ax.plot(t, Phi)
        plt.ylabel('Auslenkung $\phi(t)$')
        plt.xlabel('Zeit t')
        plt.show()