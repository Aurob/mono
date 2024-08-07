
const loadModule = async () => {
    const urlParams = new URLSearchParams(window.location.search);
    const paramValue = urlParams.get('l') || urlParams.get('level');
    
    let modulePath = '';
    if (paramValue) {
        modulePath = `/scenes/levels/${paramValue}.js`;
        
        try {
            const module = await import(modulePath);
            
            if (module && Level) {
                Level.load();
            }
            
        } catch (error) {
            console.error('Error loading module:', error);
        }
    }

  };

loadModule();